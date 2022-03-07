package hr.atos.praksa.tictactoe.model;

import java.util.ArrayList;

public class Match {
    private String player1, player2, winner;
    private ArrayList<Move> moves;

    public Match(String player1, String player2, String winner){
        this.player1 = player1;
        this.player2 = player2;
        this.winner = winner;
        moves = new ArrayList<Move>();
    }


    public String getPlayer1() {
        return player1;
    }

    public void setPlayer1(String player1) {
        this.player1 = player1;
    }

    public String getPlayer2() {
        return player2;
    }

    public void setPlayer2(String player2) {
        this.player2 = player2;
    }

    public String getWinner() {
        return winner;
    }

    public void setWinner(String winner) {
        this.winner = winner;
    }
}
