unit Ratings;
interface
const InitialRating = 0.0;
type Result = 0..2;
procedure Update(var First, Second: Real; {const} Result: Result);
implementation
procedure Update(var First, Second: Real; {const} Result: Result);
begin
    WriteLn('Test!')
end;
end.