import { BaseResponse } from './BaseResponse';

export interface MessageBase {
  text: string;
  created_by: number;
  room_id: number;
}

export interface Message extends MessageBase {
  id: string;
}

export interface MessageCreatedResponse extends BaseResponse {
  message: Message;
}

export interface MessageDeletedResponse extends BaseResponse {
  message: Message;
}

export interface MessagesFetchedResponse extends BaseResponse {
  messages: Message[];
}

export interface MessageFetchedResponse extends BaseResponse {
  message: Message;
}

export interface MessageUpdatedResponse extends BaseResponse {
  message: Message;
}
