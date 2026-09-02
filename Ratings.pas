unit Ratings;
interface
const InitialRating = 0.0;
type Result = 0..2;
procedure Update(var First, Second: Real; Result: Result);
implementation
const C = ln(10) / 25;{unit Math!}
procedure Update(var First, Second: Real; Result: Result);
var Increase: Real;
begin
    Increase := Result - 2 / (Exp(C * (Second - First)) + 1);
    Inc(First, Increase);
    Dec(Second, Increase)
end;
end.