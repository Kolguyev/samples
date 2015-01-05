
public class Unit implements IUnit {

    private String name;
    private int x;
    private int y;

    public Unit(String name, int x, int y) {
        this.name = name;
        this.x = x;
        this.y = y;
    }

    public void ExecuteCommand(ICommand command) {
        System.out.println(this.name + " now executes command " + command.getClass().getName() + ".");
        command.Execute(this);
    }

    public String StatusString() {
        return this.name + " is at (" + this.x + ", " + this.y + ").";
    }

    public void ChangeXY(int deltaX, int deltaY) {
        this.x = this.x + deltaX;
        this.y = this.y + deltaY;
    }

}
