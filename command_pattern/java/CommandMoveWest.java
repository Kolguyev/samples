
public class CommandMoveWest implements ICommand {

    public void Execute(IUnit unit) {
        unit.ChangeXY(-1, 0);
    }

}
