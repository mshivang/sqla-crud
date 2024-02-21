import { BaseResponse } from './BaseResponse';

export interface RoomBase {
  name: string;
  created_by: number;
}

export interface Room extends RoomBase {
  id: number;
}

export interface RoomCreatedResponse extends BaseResponse {
  room: Room;
}

export interface RoomDeletedResponse extends BaseResponse {
  room: Room;
}

export interface RoomsFetchedResponse extends BaseResponse {
  rooms: Room[];
}

export interface RoomFetchedResponse extends BaseResponse {
  room: Room;
}

export interface RoomUpdatedResponse extends BaseResponse {
  room: Room;
}
