import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import {
  Room,
  RoomBase,
  RoomCreatedResponse,
  RoomFetchedResponse,
} from '../domain/entity';
import { environment } from '../environments';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class RoomService {
  constructor(private http: HttpClient) {}

  roomSubject: BehaviorSubject<Room | null> = new BehaviorSubject<Room | null>(
    null
  );

  setRoom(room: Room | null): void {
    this.roomSubject.next(room);
  }

  getRoom$(): Observable<Room | null> {
    return this.roomSubject.asObservable();
  }

  createRoom$(room: RoomBase): Observable<RoomCreatedResponse> {
    return this.http.post<RoomCreatedResponse>(
      `${environment.baseUrl}/rooms`,
      room
    );
  }

  fetchRoom$(roomId: string): Observable<RoomFetchedResponse> {
    return this.http.get<RoomFetchedResponse>(
      `${environment.baseUrl}/rooms/${roomId}`
    );
  }
}
