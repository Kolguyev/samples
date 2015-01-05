import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        System.out.println("---Start---");

        // Create list of commands to execute
        List<ICommand> commands = new ArrayList<ICommand>();
        commands.add(new CommandMoveNorth());
        commands.add(new CommandMoveEast());
        commands.add(new CommandMoveSouth());
        commands.add(new CommandMoveSouth());
        commands.add(new CommandMoveWest());
        commands.add(new CommandMoveWest());
        commands.add(new CommandMoveNorth());
        commands.add(new CommandMoveEast());

        // Instantiate a unit that executes the commands
        Unit unit = new Unit("Lars", 5, 5);
        System.out.println(unit.StatusString());

        for (int i = 0;i<commands.size();i++) {
            ICommand command = commands.get(i);
            unit.ExecuteCommand(command);
            System.out.println(unit.StatusString());
        }
        System.out.println("---Finished---");
    }
}
