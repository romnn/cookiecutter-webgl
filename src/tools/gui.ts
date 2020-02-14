import dat from 'dat.gui';
import { app } from '../main';


export class AppOptions {
    algorithm = 'Algorithm 1';
    speed = 0.03;
    wireframe = false;
    color = "#00bfa5";
    execute = () => { alert("Function was called") };
}

export class AppGui {
    gui: dat.GUI
  
    constructor() {
        this.gui = new dat.GUI();
        let controls = new AppOptions();
        this.gui.add(controls, 'algorithm', [ 'Algorithm 1', 'Algorithm 2', 'Algorithm 3' ] );
        var speedListener = this.gui.add(controls, 'speed').min(0).max(0.07).step(0.0001).listen();
        var wireframeListener = this.gui.add(controls, 'wireframe').listen();
        var cubeColorListener = this.gui.addColor(controls, 'color').listen();
        this.gui.add(controls, 'execute');
        this.gui.open();
        
        wireframeListener.onChange((enabled: boolean) => app.cube.material.wireframe = enabled);
        cubeColorListener.onChange((color: string) => app.cube.material.emissive.setHex(parseInt(color.replace("#", "0x"), 16)));
        speedListener.onChange((speed: number) => app.speed = speed);

        this.gui.domElement.classList.add('custom-gui');
    }
}