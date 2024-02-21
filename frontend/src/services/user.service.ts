import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {
  LoginParams,
  LoginUserResponse,
  RefreshTokenResponce,
  User,
  UserAddedResponse,
  UserBase,
  UserDeletedResponse,
  UsersFetchedResponse,
} from '../domain/entity';
import { BehaviorSubject, Observable } from 'rxjs';
import { environment } from '../environments';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  constructor(private http: HttpClient) {}
  userSubject: BehaviorSubject<User | null> = new BehaviorSubject<User | null>(
    null
  );

  setUser(user: User): void {
    localStorage.setItem('user', JSON.stringify(user));
    this.userSubject.next(user);
  }

  getUser$(): Observable<User | null> {
    return this.userSubject.asObservable();
  }

  logoutUser(): void {
    this.userSubject.next(null);
    localStorage.removeItem('user');
  }

  loginUser$(params: LoginParams): Observable<LoginUserResponse> {
    return this.http.post<LoginUserResponse>(
      `${environment.authUrl}/dj-rest-auth/login/`,
      params,
      {
        withCredentials: true,
      }
    );
  }

  fetchUsers$(): Observable<UsersFetchedResponse> {
    return this.http.get<UsersFetchedResponse>(
      `${environment.authUrl}/api/users/`,
      {
        withCredentials: true,
      }
    );
  }

  registerUser$(user: UserBase): Observable<UserAddedResponse> {
    return this.http.post<UserAddedResponse>(
      `${environment.authUrl}/dj-rest-auth/registration/`,
      user,
      {
        withCredentials: true,
      }
    );
  }

  deleteUser$(id: number): Observable<UserDeletedResponse> {
    return this.http.delete<UserDeletedResponse>(
      `${environment.authUrl}/api/users/${id}`,
      {
        withCredentials: true,
      }
    );
  }

  refreshToken$(): Observable<RefreshTokenResponce> {
    return this.http.post<RefreshTokenResponce>(
      `${environment.authUrl}/dj-rest-auth/token/refresh/`,
      {},
      {
        withCredentials: true,
      }
    );
  }

  resetPassword$(email: string): Observable<{ detail: string }> {
    return this.http.post<{ detail: string }>(
      `${environment.authUrl}/dj-rest-auth/password/reset/`,
      { email },
      { withCredentials: true }
    );
  }
}
