import { Component, OnDestroy, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from '../components/navbar/navbar.component';
import { UserService } from '../services/user.service';
import { RoomService } from '../services/room.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, NavbarComponent],
  providers: [UserService, RoomService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'frontend';
  constructor(private userService: UserService) {}

  ngOnInit(): void {
    const userString = localStorage.getItem('user');
    const user = userString ? JSON.parse(userString) : null;
    if (userString) {
      this.userService.setUser(user);
    }
  }

  ngOnDestroy(): void {}
}
