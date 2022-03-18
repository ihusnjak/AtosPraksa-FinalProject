package hr.atos.praksa.tictactoecpp.model;

import java.io.Serializable;

public class Move implements Serializable {
    private int move_number, affected_field;

    public Move(int moveNo, int playedField){
        this.move_number = moveNo;
        this.affected_field = playedField;
    }

    public int getMoveNo() {
        return move_number;
    }

    public void setMoveNo(int moveNo) {
        this.move_number = moveNo;
    }

    public int getAffected_field() {
        return affected_field;
    }

    public void setAffected_field(int affected_field) {
        this.affected_field = affected_field;
    }


}
