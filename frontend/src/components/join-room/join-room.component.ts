import { Component } from '@angular/core';
import {
  FormControl,
  Validators,
  FormsModule,
  ReactiveFormsModule,
} from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-join-room',
  standalone: true,
  imports: [
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule,
    MatButtonModule,
    RouterModule,
  ],
  templateUrl: './join-room.component.html',
  styleUrl: './join-room.component.css',
})
export class JoinRoomComponent {
  roomIdFormControl = new FormControl('', [Validators.required]);

  constructor(public router: Router) {}

  joinRoom() {
    const roomId = this.roomIdFormControl.value;
    this.roomIdFormControl.setValue('');
    this.router.navigate(['room', roomId]);
  }
}
