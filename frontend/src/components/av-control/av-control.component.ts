import { Component, OnDestroy, OnInit } from '@angular/core';
import { RoomService } from '../../services/room.service';
import { Router, RouterModule } from '@angular/router';
import { Room } from '../../domain/entity';
import { Subscription } from 'rxjs';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-av-control',
  standalone: true,
  imports: [RouterModule, CommonModule],
  templateUrl: './av-control.component.html',
  styleUrl: './av-control.component.css',
})
export class AvControlComponent implements OnInit, OnDestroy {
  constructor(private roomService: RoomService, private router: Router) {}

  public room?: Room;
  private subscription!: Subscription;

  ngOnInit(): void {
    this.subscription = this.roomService.getRoom$().subscribe(
      (room) => {
        if (room) {
          this.room = room;
        }
      },
      (error) => {
        console.error('Error getting room:', error);
        this.router.navigate(['']);
      }
    );
  }

  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
