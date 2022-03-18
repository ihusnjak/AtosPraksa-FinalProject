package hr.atos.praksa.tictactoecpp.model;

import java.io.Serializable;
import java.util.ArrayList;

public class Match implements Serializable {
    private String player1, player2, winner;
    private int id;
    private ArrayList<Move> moves;

    public Match(String player1, String player2, String winner, int id){
        this.player1 = player1;
        this.player2 = player2;
        this.winner = winner;
        this.id = id;
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

    public ArrayList<Move> getMovesList(){ return this.moves; }

    public void addMove(Move move){
        this.moves.add(move);
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
}
