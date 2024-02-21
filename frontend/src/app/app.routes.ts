import { Routes } from '@angular/router';
import { RoomComponent } from '../pages/room/room.component';
import { HomeComponent } from '../pages/home/home.component';
import { LoginComponent } from '../pages/login/login.component';

export const routes: Routes = [
  { path: 'room/:id', component: RoomComponent },
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
];
