#include <iostream>
#include <cstdlib>
#include <ctime>
#include <set>

#define str string

void print_play_field(std::str play_field[3][3], std::str current_player)
{
	for (int i = 40; i > 0; i--)
	{
		std::cout << std::endl;
	}

	std::cout << "Nächster Zug : " << current_player << std::endl;

	for (int i = 0; i < 3; i++)
	{
		std::cout << play_field[i][0] << " ";
		std::cout << play_field[i][1] << " ";
		std::cout << play_field[i][2] << std::endl;
	}
}

std::str check_win(std::str play_field[3][3])
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
	std::str play_field[3][3] = {{"_", "_", "_"},
							   {"_", "_", "_"},
							   {"_", "_", "_"}};
	std::str player1 = "X", player2 = "O";
	std::str current_player;
	std::set<int> allowed_entrys = {1, 2, 3};
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

		std::str winner = check_win(play_field);
		if (winner == player1 || winner == player2)
		{
			std::cout << "Der Gewinner des Spiels ist : " << winner << std::endl;
			break;
		}

		std::cout << "Gebe die Zeile des neuen Eintrags ein : ";
		std::cin >> new_line;
		std::cout << "Gebe die Spalte des neuen Eintrags ein : ";
		std::cin >> new_column;

		if (allowed_entrys.find(new_line) == allowed_entrys.end() || allowed_entrys.find(new_column) == allowed_entrys.end())
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