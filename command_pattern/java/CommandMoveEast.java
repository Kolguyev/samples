
public class CommandMoveEast implements ICommand {

    public void Execute(IUnit unit) {
        unit.ChangeXY(1, 0);
    }
}
