package hr.atos.praksa.tictactoe.listeners;

import java.util.ArrayList;

import hr.atos.praksa.tictactoe.model.Match;

public interface UiListener {
    void onModificationPerformed(ArrayList<Match> matches);
}
