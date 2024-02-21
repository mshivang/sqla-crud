export type ResponseStatus = 'success' | 'fail';

export interface BaseResponse {
  status: ResponseStatus;
  detail?: string;
}
