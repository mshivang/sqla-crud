import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { RoomService } from '../../services/room.service';
import { ChatsComponent } from '../../components/chats/chats.component';
import { AvControlComponent } from '../../components/av-control/av-control.component';
import { switchMap } from 'rxjs/operators';
import { of } from 'rxjs';

@Component({
  selector: 'app-room',
  standalone: true,
  templateUrl: './room.component.html',
  imports: [ChatsComponent, AvControlComponent],
  styleUrls: ['./room.component.css'],
})
export class RoomComponent implements OnInit, OnDestroy {
  constructor(
    private route: ActivatedRoute,
    private roomService: RoomService
  ) {}

  ngOnInit() {
    // Get the roomId from the route parameters
    this.route.params
      .pipe(
        switchMap((params) => {
          const roomId = params['id'];
          if (roomId) {
            // Fetch the room based on the roomId
            return this.roomService.fetchRoom$(roomId);
          } else {
            // If roomId is not present, return an observable with null
            return of(null);
          }
        })
      )
      .subscribe((res) => {
        // Set the room in the RoomService
        if (res) {
          this.roomService.setRoom(res.room);
        }
      });
  }

  ngOnDestroy() {
    // Remove the room from the RoomService when the component is destroyed
    this.roomService.setRoom(null);
  }
}
