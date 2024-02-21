import { Component, OnDestroy, OnInit } from '@angular/core';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import {
  FormControl,
  FormsModule,
  Validators,
  ReactiveFormsModule,
} from '@angular/forms';
import { ChatService } from '../../services/chat.service';
import { Message, MessageBase } from '../../domain/entity/Message';
import { Subscription } from 'rxjs';
import { RoomService } from '../../services/room.service';
import { UserService } from '../../services/user.service';
import { CommonModule } from '@angular/common';
import { Router, RouterModule } from '@angular/router';
import { MessageComponent } from '../message/message.component';

@Component({
  selector: 'app-chats',
  standalone: true,
  imports: [
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule,
    CommonModule,
    RouterModule,
    MessageComponent
  ],
  templateUrl: './chats.component.html',
  styleUrl: './chats.component.css',
})
export class ChatsComponent implements OnInit, OnDestroy {
  private subscription!: Subscription;
  public userId?: number;
  public roomId?: number;

  constructor(
    private chatService: ChatService,
    private roomService: RoomService,
    private userService: UserService,
    private router: Router
  ) {}

  messageControl = new FormControl('', [
    Validators.required,
    Validators.min(2),
    Validators.max(500),
  ]);

  public messages: Message[] = [];

  ngOnInit() {
    this.userService.getUser$().subscribe(
      (user) => {
        if (user) {
          this.userId = user.pk;
          console.log('User:', user);
          this.tryConnect();
        } else {
          this.router.navigate(['login']);
        }
      },
      (error) => {
        console.error('Error getting user:', error);
        // Handle error if needed
      }
    );

    this.roomService.getRoom$().subscribe(
      (room) => {
        if (room) {
          this.roomId = room.id;
          console.log('Room:', room);
          this.tryConnect();
        }
      },
      (error) => {
        console.error('Error getting room:', error);
        this.router.navigate(['']);
      }
    );
  }

  ngOnDestroy() {
    // Close the WebSocket connection when the component is destroyed
    this.chatService.closeConnection();
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  private tryConnect() {
    // Try to connect only when both userId and roomId are available
    if (this.userId && this.roomId) {
      this.chatService.connect(this.roomId, this.userId);

      // Subscribe to incoming messages
      this.subscription = this.chatService.receiveMessage().subscribe(
        (message) => {
          const currentMessages = this.messages;
          const updatedMessages = [...currentMessages, message];
          this.messages = updatedMessages;
        },
        (error) => {
          console.error('Error receiving message:', error);
          // Handle error if needed
        }
      );
    }
  }

  sendMessage() {
    const messageText = this.messageControl.value;

    if (!messageText) {
      alert('Please enter a message!');
      return;
    }

    if (!this.userId || !this.roomId) {
      // Handle the absence of userId or roomId
      alert('User ID or Room ID is missing. Cannot send the message.');
      return;
    }

    const messageObject: MessageBase = {
      text: messageText!,
      created_by: this.userId,
      room_id: this.roomId,
    };

    this.chatService.sendMessage(messageObject);

    this.messageControl.setValue(null);
    this.messageControl.setErrors(null);
  }
}
