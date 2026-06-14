[Setup]
AppId={{C789-Ваш-Уникальный-GUID-Тут}}
AppName=Text 2 CSV Converter
AppVersion=0.2.0-alpha
AppPublisher=Oleh0789
DefaultDirName={autopf}\Text2CSVConverter
DefaultGroupName=Text 2 CSV Converter
; Куда сохранить готовый файл установщика
OutputDir=.\installer_output
OutputBaseFilename=text2csv_setup_v0.2.0-alpha
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Берем наш собранный PyInstaller-ом файл из папки dist
Source: ".\dist\txt2csv_converter.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Text 2 CSV Converter"; Filename: "{app}\txt2csv_converter.exe"
Name: "{commondesktop}\Text 2 CSV Converter"; Filename: "{app}\txt2csv_converter.exe"; Tasks: desktopicon

[Run]
; Предложить запустить программу после установки
Filename: "{app}\txt2csv_converter.exe"; Description: "{cm:LaunchProgram,Text 2 CSV Converter}"; Flags: nowait postinstall skipifsilent