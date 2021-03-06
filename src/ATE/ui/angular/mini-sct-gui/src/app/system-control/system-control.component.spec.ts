import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { DebugElement } from '@angular/core';
import { SystemControlComponent } from './system-control.component';
import { InputComponent } from './../basic-ui-elements/input/input.component';
import { ButtonComponent } from './../basic-ui-elements/button/button.component';
import { CardComponent } from './../basic-ui-elements/card/card.component';
import { TestExecutionComponent } from './test-execution/test-execution.component';
import { TestOptionComponent } from './test-option/test-option.component';
import { LotHandlingComponent } from './lot-handling/lot-handling.component';
import { CheckboxComponent } from '../basic-ui-elements/checkbox/checkbox.component';
import { By } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

describe('SystemControlComponent', () => {
  let component: SystemControlComponent;
  let fixture: ComponentFixture<SystemControlComponent>;
  let debugElement: DebugElement;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        SystemControlComponent,
        TestExecutionComponent,
        TestOptionComponent,
        LotHandlingComponent,
        CardComponent,
        InputComponent,
        ButtonComponent,
        CheckboxComponent
      ],
      imports: [FormsModule],
      schemas: []
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SystemControlComponent);
    component = fixture.componentInstance;
    debugElement = fixture.debugElement;
    fixture.detectChanges();
  });

  it('should create system control component', () => {
    expect(component).toBeDefined();
  });

  it('should support labelText', async(() => {

    // check app-card header text
    let expectedHeaderText = 'System Control';
    let appCardHeader = debugElement.nativeElement.querySelector('app-card .header');
    expect(expectedHeaderText).toEqual(component.systemControlCardConfiguration.labelText);
    expect(appCardHeader.textContent).toContain(expectedHeaderText);

    // check option label text
    let optionDebugElement = debugElement.query(By.directive(TestOptionComponent));
    let expectedOptionsLabelText = 'Options';
    let optionsAppCardHeader = debugElement.nativeElement.querySelector('#option app-card .header');
    expect(expectedOptionsLabelText).toEqual(optionDebugElement.context.testOptionCardConfiguration.labelText);
    expect(optionsAppCardHeader.textContent).toContain(expectedOptionsLabelText);
  }));

  describe('Tags of the other component type', () => {
    it('should contain an app-card tag', async(() => {
      let componentElement = debugElement.nativeElement.querySelector('app-card');
      expect(componentElement).not.toEqual(null);
    }));

    it('should contain an app-lot-handling tag', async(() => {
      let componentElement = debugElement.nativeElement.querySelector('app-lot-handling');
      expect(componentElement).not.toEqual(null);
    }));

    it('should contain an app-test-execution tag', async(() => {
      let componentElement = debugElement.nativeElement.querySelector('app-test-execution');
      expect(componentElement).not.toEqual(null);
    }));

    it('should contain an app-test-option tag', async(() => {
      let componentElement = debugElement.nativeElement.querySelector('app-test-option');
      expect(componentElement).not.toEqual(null);
    }));
  });
});
