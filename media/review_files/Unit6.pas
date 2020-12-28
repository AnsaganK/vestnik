unit Unit6;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, ExtCtrls, jpeg;

type
  TZastavka = class(TForm)
    Image1: TImage;
    Timer1: TTimer;
    procedure Timer1Timer(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Zastavka: TZastavka;

implementation

{$R *.dfm}

procedure TZastavka.Timer1Timer(Sender: TObject);
begin
Close();
end;

end.
