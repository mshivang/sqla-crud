import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';
import { MessageBase } from '../domain/entity/Message';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ChatService {
  private socket$: WebSocketSubject<any> | undefined;

  constructor() {}

  connect(roomId: number, clientId: number): void {
    const url = `ws://localhost:8000/ws/${roomId}/${clientId}`;
    console.log(url);
    this.socket$ = webSocket(url);
  }

  sendMessage(message: MessageBase): void {
    if (this.socket$) {
      this.socket$.next(message);
    }
  }

  receiveMessage(): Observable<any> {
    return this.socket$ ? this.socket$.asObservable() : new Observable();
  }

  closeConnection(): void {
    if (this.socket$) {
      this.socket$.complete();
    }
  }
}
