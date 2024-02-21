import { Component, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatDividerModule } from '@angular/material/divider';
import { Router, RouterModule } from '@angular/router';
import {
  FormControl,
  FormsModule,
  Validators,
  ReactiveFormsModule,
} from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { UserService } from '../../services/user.service';
import { LoginParams } from '../../domain/entity';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    MatButtonModule,
    MatIconModule,
    MatFormFieldModule,
    MatInputModule,
    MatCheckboxModule,
    MatDividerModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent implements OnInit {
  constructor(
    private userService: UserService,
    private router: Router,
    private _snackBar: MatSnackBar
  ) {}

  // Snackbar Configuration
  durationInSeconds = 5;

  openSnackBar(message: string) {
    this._snackBar.open(message, undefined, {
      duration: 3000,
    });
  }

  // Initialization
  ngOnInit(): void {}

  // Form configuration
  userNameControl = new FormControl('', [
    Validators.required,
    Validators.min(2),
    Validators.max(10),
  ]);

  passwordControl = new FormControl('', [
    Validators.required,
    Validators.min(8),
    Validators.max(100),
    Validators.pattern(/^[a-zA-Z0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]{8,100}$/),
  ]);

  public onSubmit(): void {
    // Check if any of the controls have errors
    if (this.userNameControl.valid && this.passwordControl.valid) {
      const formValue: LoginParams = {
        username: this.userNameControl.value!,
        password: this.passwordControl.value!,
      };

      // Run API Call
      this.userService.loginUser$(formValue).subscribe(
        (val) => {
          this.userService.setUser(val.user);

          if (val.user.is_superuser) {
            this.router.navigate(['dashboard']);
          } else {
            this.router.navigate(['']);
          }
        },
        (res) => {
          this.openSnackBar(res.error.non_field_errors[0]);
        }
      );

      // Reset Form
      this.userNameControl.reset();
      this.passwordControl.reset();
      this.userNameControl.setErrors(null);
      this.passwordControl.setErrors(null);
    } else {
      // Handle form control errors
      this.openSnackBar(
        'Form controls have errors. Please check and try again.'
      );
    }
  }
}
