import os
from openai import OpenAI



def ai_notes(test):

    api_key='OPENROUTER_API_KEY_HERE'

    os.environ["OPENAI_API_KEY"] = api_key

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key)

    # create the prompt based on the selected test
    context = (
        f"Class: {test['klasa']}\n"
        f"Type: {test['sprawdzian_or_kartkowka']}\n"
        f"Subject: {test['subject']}\n"
        f"Topic: {test['topic']}\n"
    )

    question = ("Na podstawie podanych informacji o klasie (ucznia w Polskim liceum, "
        "rozszerzenia matematyki, fizyki, informatyki), rodzaju testu, przedmiotu "
        "z którego jest ten test i tematu, wygeneruj notatke, ktora przygotuje ucznia "
        "do tego testu. Notatka powinna byc napisana z uzyciem tylko znakow ASCII "
        "(bez emoji, bez polskich znakow). "
        "\n\nNotatka powinna zawierac:\n"
        "1. Pojecia zwiazane z tym tematem (nie wykraczaj poza program klasy; max 100 slow)\n"
        "2. 5 przykladowych zadan z krotkim wytlumaczeniem jak je rozwiazac\n"
        "3. Przykladowy test z 10 zadaniami (pasujacymi do klasy), a po 3 linijkach przerwy "
        "napisz sekcje 'ODPOWIEDZI' z odpowiedziami i bardzo krotkimi wytlumaczeniami.")

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3.1:free",
        messages=[
            {"role": "system", "content": "Jesteś pomocnym korepetytorem,"
                                          " który przygotowywuje do testów"},
            {"role": "user", "content": f"{context}\n\nTask: {question}"}
        ]
    )

    print("\nAI Notes:\n")
    print(response.choices[0].message.content)
    print("\n---------------------------------------------\n")