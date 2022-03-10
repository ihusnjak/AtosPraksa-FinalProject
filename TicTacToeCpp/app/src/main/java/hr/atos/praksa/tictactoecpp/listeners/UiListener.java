package hr.atos.praksa.tictactoecpp.listeners;

import java.util.ArrayList;

import hr.atos.praksa.tictactoecpp.model.Match;

public interface UiListener {
    void onModificationPerformed(ArrayList<Match> matches);
}
