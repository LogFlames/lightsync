string path = @"C:/Users/Elias Lundell/code/lightsync/cycle.txt";

if (!Path.Exists(path))
{
    File.WriteAllText(path, "3");
}

string text = File.ReadAllText(path);
if (text == null)
{
    text = "3";
}

int cycle;
if (!int.TryParse(text, out cycle))
{
    cycle = 3;
}

cycle = (cycle + 1) % 4;

File.WriteAllText(path, cycle.ToString());