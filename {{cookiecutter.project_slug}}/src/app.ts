import { Color, PointLight, PerspectiveCamera, Scene, Vector3, WebGLRenderer } from 'three';
import { Cube } from './cube';
import { AppStats } from './tools/stats';
import { AppGui } from './tools/gui';
import { AppOrbit } from './tools/orbit';
import settings from './config/settings';

export class App {
    private readonly stats?: AppStats;
    private readonly gui?: AppGui;
    private readonly orbit?: AppOrbit;
    private readonly scene = new Scene();
    private readonly camera = new PerspectiveCamera(45, innerWidth / innerHeight, 0.1, 10000);
    private readonly canvas = document.getElementById('main-canvas') as HTMLCanvasElement;
    private readonly renderer = new WebGLRenderer({
        antialias: true,
        // alpha: !settings.backgroundColor,
        canvas: this.canvas,
    });

    cube: Cube;
    speed = 0.03;

    constructor() {
        this.cube = new Cube(100, new Color(0xffc107), new Color(0x00bfa5));

        const lights = [
            new PointLight(0xffffff, 0.2, 0),
            new PointLight(0xffffff, 0.2, 0),
            new PointLight(0xffffff, 0.2, 0),
        ];
        lights[0].position.set(0, 200, 0);
        lights[1].position.set(100, 200, 100);
        lights[2].position.set(-100, -200, -100);

        this.scene.add(this.cube);
        for (const light of lights) {
            this.scene.add(light);
        }

        this.camera.position.set(200, 200, 200);
        this.camera.lookAt(new Vector3(0, 0, 0));

        this.renderer.setSize(innerWidth, innerHeight);
        this.renderer.setClearColor(new Color(0, 0, 0));

        if (settings.stats) this.stats = new AppStats();
        if (settings.gui) this.gui = new AppGui();
        if (settings.orbit) this.orbit = new AppOrbit(this.camera, this.canvas);

        this.render();
    }

    private adjustCanvasSize(): void {
        this.renderer.setSize(innerWidth, innerHeight);
        this.camera.aspect = innerWidth / innerHeight;
        this.camera.updateProjectionMatrix();
    }

    private render(): void {
        this.stats?.start();
        this.renderer.render(this.scene, this.camera);
        this.stats?.end();
        requestAnimationFrame(() => this.render());

        this.adjustCanvasSize();
        this.cube.rotateY(this.speed);
    }
}
