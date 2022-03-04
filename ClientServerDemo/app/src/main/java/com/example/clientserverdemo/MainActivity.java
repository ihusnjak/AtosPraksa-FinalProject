package com.example.clientserverdemo;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.android.material.textfield.TextInputEditText;

public class MainActivity extends AppCompatActivity implements UiListener {

    private Button button;
    private TextView textView;
    private TextInputEditText textInputEditText;
    private Logic logic;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setupUiElements();
        logic = Logic.getInstance();
        logic.setListener(this);
    }

    private void setupUiElements() {
        button = findViewById(R.id.button);
        textView = findViewById(R.id.textView);
        textInputEditText = findViewById(R.id.textInputEditText);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                logic.performCalculation(textInputEditText.getText().toString());
            }
        });
    }

    @Override
    public void onModificationPerformed(String firstName, String lastName) {
        textView.setVisibility(View.VISIBLE);
        textView.setText("First Name: " + firstName + "\n" + "Last Name: " + lastName + "\n");
    }
}