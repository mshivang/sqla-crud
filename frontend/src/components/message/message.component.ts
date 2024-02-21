import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';
import { Message } from '../../domain/entity/Message';

@Component({
  selector: 'app-message',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './message.component.html',
  styleUrl: './message.component.css',
})
export class MessageComponent {
  @Input() message!: Message;
  @Input() isOwn: boolean = false;
}
