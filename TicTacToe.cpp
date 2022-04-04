#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void print_play_field(string play_field[3][3], string current_player)
{
	for (int i = 40; i > 0; i--)
	{
		cout << endl;
	}

	cout << "Nächster Zug : " << current_player << endl;

	for (int i = 0; i < 3; i++)
	{
		cout << play_field[i][0] << " ";
		cout << play_field[i][1] << " ";
		cout << play_field[i][2] << endl;
	}
}

string check_win(string play_field[3][3])
{
	// horizontal
	for (int i = 0; i < 3; i++)
	{
		if (play_field[i][0] == play_field[i][1] && play_field[i][1] == play_field[i][2])
		{
			if (play_field[i][0] != "_")
			{
				return play_field[i][0];
			}
		}
	}

	// vertical
	for (int i = 0; i < 3; i++)
	{
		if (play_field[0][i] == play_field[1][i] && play_field[1][i] == play_field[2][i])
		{
			if (play_field[0][i] != "_")
			{
				return play_field[0][i];
			}
		}
	}

	//diagonal1
	if (play_field[0][0] == play_field[1][1] && play_field[1][1] == play_field[2][2])
	{
		if (play_field[0][0] != "_")
			{
				return play_field[0][0];
			}
	}

	//diagonal2
	if (play_field[0][2] == play_field[1][1] && play_field[1][1] == play_field[2][0])
	{
		if (play_field[0][2] != "_")
			{
				return play_field[0][2];
			}
	}

	return "";
}

int main()
{
	string play_field[3][3] = {{"_", "_", "_"},
							   {"_", "_", "_"},
							   {"_", "_", "_"}};
	string player1 = "X", player2 = "O";
	string current_player;
	string allowed_entrys[3] = {"1", "2", "3"};
	int new_line, new_column;

	srand(time(0));
	if ((rand() % 2) == 1)
	{
		current_player = player1;
	}
	else
	{
		current_player = player2;
	}

	while (1)
	{

		print_play_field(play_field, current_player);

		string winner = check_win(play_field);
		if (winner == player1 || winner == player2)
		{
			cout << "Der Gewinner des Spiels ist : " << winner << endl;
			break;
		}

		cout << "Gebe die Zeile des neuen Eintrags ein : ";
		cin >> new_line;
		cout << "Gebe die Spalte des neuen Eintrags ein : ";
		cin >> new_column;

		if (new_line > 3 || new_column > 3)
		{
			continue;
		}

		if (play_field[new_line - 1][new_column - 1] == "_")
		{
			play_field[new_line - 1][new_column - 1] = current_player;

			if (current_player == player1)
			{
				current_player = player2;
			}

			else
			{
				current_player = player1;
			}
		}
	}
}