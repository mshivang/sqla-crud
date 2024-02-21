import { ApplicationConfig, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideAnimations } from '@angular/platform-browser/animations';

import { routes } from './app.routes';
// import { SocketIoConfig, SocketIoModule } from 'ngx-socket-io';
// import { environment } from '../environments';

// const config: SocketIoConfig = {
//   url: 'http://127.0.0.1:8000/ws',
//   options: {
//     transports: ['websocket'],
//   },
// };

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideAnimations(),
    // importProvidersFrom(SocketIoModule.forRoot(config)),
  ],
};
