# Vyhledávač dne
Co se stane, když spojíte prokrastinujícího člověka a "volný" večer ? Já nevím, ale tady jsem vytvořil nějakej program. Už jste si někdy říkali kdy bude nejbližší Pátek 13. ? Nebo kdy bude třeba nejbližší Pondělí 1. ? Díky tomuto programu to lze zjistit během pár kliknutí. Jednoduše řečeno, program vyhledává nejbližší kombinaci Název dne-Číslo dne (nevím jak to pojmenovat) od počátečního data. 

## Požadavky
Well... budete potřebovat Python... duh... nejlépe ten z [ofiko stránek](https://www.python.org). Pokud nemáte z nějakého důvodu tkinter nainstalovanej s Pythonem tak ho nainstalujte pomocí `pip install tk`. Navíc budete potřebovat knihovnu `tkcalendar`, ta se dá stáhnout pomocí `pip install tkcalendar`. Nevím, jestli je na jiných OS potřeba jiný způsob, já používám Windows a tak to píšu podle sebe.

## Použití
Po spuštění by se mělo otevřít okno. V tom okně je v horní části počáteční datum. To je datum, od kterého to hledá hledaný den. Po zapnutí programu je v počátečním datu dnešní datum. Pokud chceme vybrat jiné, klikneme na kalendář, vyhledáme požadované počáteční datum a stikneme `Vybrat datum`, čímž se uloží vybraný den. Hledaný den lze určit pomocí nabídek v prostřední části. Stisknutím tlačítka `Vyhledat` to najde nejbližší budoucí den odpovídající hledanému dnu. Pokud zadáme hledaný den stejný jako startovací (např. Je 01.01.2023 a my dáme hledat Neděle 1.), najde to nejbližší budoucí vyhovující den, neoznačí to startovací den (V našem příkladě to vyhledá 1.10.2023).

## Něco závěrem
Nejsem expert, a toto byl program jen tak pro zábavu. S Githubem neumím a toto je reálně první pokus o cokoliv smysluplného tady. Tento program není světoborný, a věřím, že existuje 98 tisíc způsobů jak to udělat lépe. Přehlednost sice nemusí být nejlepší, ovšem mně vyhovuje.
