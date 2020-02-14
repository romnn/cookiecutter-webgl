import Stats from 'stats.js';

export class AppStats {
  stats: Stats

  constructor() {
    this.stats = new Stats();
    this.stats.showPanel(0);
    document.body.appendChild(this.stats.dom);
  }

  start() {
    this.stats.begin()
  }

  end() {
    this.stats.end()
  }

}
