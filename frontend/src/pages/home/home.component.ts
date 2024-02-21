import { Component } from '@angular/core';
import { CreateRoomComponent } from '../../components/create-room/create-room.component';
import { JoinRoomComponent } from '../../components/join-room/join-room.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CreateRoomComponent, JoinRoomComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
})
export class HomeComponent {}
