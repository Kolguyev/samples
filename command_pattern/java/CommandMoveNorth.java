
public class CommandMoveNorth implements ICommand {

    public void Execute(IUnit unit) {
        unit.ChangeXY(0, 1);
    }

}
