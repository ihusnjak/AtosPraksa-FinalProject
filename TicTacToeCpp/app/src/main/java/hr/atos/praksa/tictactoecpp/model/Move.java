package hr.atos.praksa.tictactoecpp.model;

import java.io.Serializable;

public class Move implements Serializable {
    private int moveNo, playedField;

    public Move(int moveNo, int playedField){
        this.moveNo = moveNo;
        this.playedField = playedField;
    }

    public int getMoveNo() {
        return moveNo;
    }

    public void setMoveNo(int moveNo) {
        this.moveNo = moveNo;
    }

    public int getPlayedField() {
        return playedField;
    }

    public void setPlayedField(int playedField) {
        this.playedField = playedField;
    }


}
