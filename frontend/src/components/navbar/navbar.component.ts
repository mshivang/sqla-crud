import { Component, OnDestroy, OnInit } from '@angular/core';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { MatDividerModule } from '@angular/material/divider';
import { Subject, takeUntil } from 'rxjs';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { User } from '../../domain/entity';
import { UserService } from '../../services/user.service';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [
    MatToolbarModule,
    CommonModule,
    RouterModule,
    MatMenuModule,
    MatIconModule,
    MatDividerModule,
    HttpClientModule,
    MatButtonModule,
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css',
})
export class NavbarComponent implements OnInit, OnDestroy {
  constructor(private userService: UserService) {}
  user: User | null = null;
  private unsubscribe = new Subject<void>();

  logout(): void {
    this.userService.logoutUser();
  }

  ngOnInit(): void {
    this.userService
      .getUser$()
      .pipe(takeUntil(this.unsubscribe))
      .subscribe((data) => {
        this.user = data;
      });
  }

  ngOnDestroy(): void {
    this.unsubscribe.next();
    this.unsubscribe.complete();
  }
}
