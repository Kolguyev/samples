
public class CommandMoveSouth implements ICommand {

    public void Execute(IUnit unit) {
        unit.ChangeXY(0, -1);
    }

}
