import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring

/-!
Exact algebraic identities used in the i=3 continuation.
These are not a formal proof of Erdős 699 or of the entire continuation.
-/

namespace Erdos699Algebra

def y0 (j _y : ℚ) : ℚ := j * (j-1) * (j-2) / 2
def y1 (j y : ℚ) : ℚ := j * (j-1) * y / 2
def y2 (j y : ℚ) : ℚ := j * y * (y-1) / 2
def y3 (_j y : ℚ) : ℚ := y * (y-1) * (y-2) / 2

theorem cross_minor (j y : ℚ) :
    y0 j y * y3 j y - y1 j y * y2 j y =
      -(j * (j-1) * y * (y-1) * (j+y-2)) / 2 := by
  unfold y0 y1 y2 y3
  ring

theorem quartic_certificate (j y : ℚ) :
    (y0 j y * y3 j y - y1 j y * y2 j y)^2 -
      4 * (y0 j y * y2 j y - (y1 j y)^2) *
          (y1 j y * y3 j y - (y2 j y)^2) =
      -(j^2 * y^2 * (j-1) * (y-1) * (j+y-2)^2 * (j+y-1)) / 4 := by
  unfold y0 y1 y2 y3
  ring

theorem cofactor_product (c f alpha beta T delta : ℚ) :
    (delta*c-T*beta) * (delta*f-T*alpha) =
      delta^2*c*f - delta*T*(c*alpha+f*beta) + T^2*alpha*beta := by
  ring

#print axioms cross_minor
#print axioms quartic_certificate
#print axioms cofactor_product

end Erdos699Algebra
