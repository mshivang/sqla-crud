import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AvControlComponent } from './av-control.component';

describe('AvControlComponent', () => {
  let component: AvControlComponent;
  let fixture: ComponentFixture<AvControlComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AvControlComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AvControlComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
