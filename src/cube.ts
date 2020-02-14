import { BoxGeometry, Color, Mesh, MeshPhongMaterial, DoubleSide } from 'three';

export class Cube extends Mesh {
  geometry: BoxGeometry
  material: MeshPhongMaterial

  constructor(size: number, color: Color, emissiveColor: Color) {
    super();
    this.geometry = new BoxGeometry(size, size, size);
    this.material = new MeshPhongMaterial({
      color: color,
      emissive: emissiveColor,
      side: DoubleSide,
    });
  }
}
