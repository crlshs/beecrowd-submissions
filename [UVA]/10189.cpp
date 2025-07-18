#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<pair<int, int>> getAdj(int i, int j, int m, int n)
{
    vector<pair<int, int>> vizinhos;
    int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int dy[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    for (int d = 0; d < 8; d++)
    {
        int x = i + dx[d];
        int y = j + dy[d];
        if (x >= 0 && x < m && y >= 0 && y < n)
        {
            vizinhos.push_back({x, y});
        }
    }

    return vizinhos;
}

int main()
{
    int m, n;
    int jogos = 0;
    vector<string> resultados;

    while (true)
    {
        cin >> m >> n;
        if (m == 0 && n == 0)
            break;
        jogos++;

        vector<vector<int>> campo(m, vector<int>(n, 0));
        vector<vector<char>> dicas(m, vector<char>(n));

        for (int i = 0; i < m; i++)
        {
            string linha;
            cin >> linha;
            for (int j = 0; j < n; j++)
            {
                dicas[i][j] = linha[j];
            }
        }

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (dicas[i][j] == '*')
                {
                    campo[i][j] = -1;
                    for (auto [x, y] : getAdj(i, j, m, n))
                    {
                        if (campo[x][y] != -1)
                            campo[x][y]++;
                    }
                }
            }
        }

        string resultado = "Field #" + to_string(jogos) + ":\n";
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (campo[i][j] == -1)
                    resultado += '*';
                else
                    resultado += char(campo[i][j] + '0');
            }
            resultado += '\n';
        }

        resultados.push_back(resultado);
    }

    for (int i = 0; i < (int)resultados.size(); i++)
    {
        cout << resultados[i];
        if (i != (int)resultados.size() - 1)
            cout << '\n';
    }

    return 0;
}
