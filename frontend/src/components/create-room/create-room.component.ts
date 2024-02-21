import { Component, OnDestroy, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { RoomService } from '../../services/room.service';
import { Router, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import {
  FormControl,
  FormsModule,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { UserService } from '../../services/user.service';
import { Subject, takeUntil } from 'rxjs';
import { User } from '../../domain/entity';

@Component({
  selector: 'app-create-room',
  standalone: true,
  imports: [
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule,
    MatButtonModule,
    RouterModule,
    HttpClientModule,
  ],
  templateUrl: './create-room.component.html',
  styleUrl: './create-room.component.css',
})
export class CreateRoomComponent implements OnInit, OnDestroy {
  roomNameFormControl = new FormControl('', [Validators.required]);
  user: User | null = null;
  private unsubscribe = new Subject<void>();

  constructor(
    public roomService: RoomService,
    public router: Router,
    public userService: UserService
  ) {}

  ngOnInit(): void {
    this.userService
      .getUser$()
      .pipe(takeUntil(this.unsubscribe))
      .subscribe((data) => {
        this.user = data;
      });
  }

  createRoom() {
    const roomName = this.roomNameFormControl.value;

    if (!roomName || !this.user) return;

    const room = {
      name: roomName,
      created_by: this.user.pk,
    };

    this.roomService.createRoom$(room).subscribe((res) => {
      if (res.status === 'success') {
        const room = res.room;
        this.router.navigate(['room', room.id]);
      }
    });
  }

  ngOnDestroy(): void {
    this.unsubscribe.next();
    this.unsubscribe.complete();
  }
}
