import { Color, PerspectiveCamera, Scene, Vector3, WebGLRenderer } from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';

export class AppOrbit {
    orbit: OrbitControls

    constructor(camera: PerspectiveCamera, dom: HTMLCanvasElement) {
        this.orbit = new OrbitControls(camera, dom);
        this.orbit.enableZoom = true;
    }
};