from agents import function_tool


@function_tool
def get_terms_and_conditions():
    """
    Returns the terms and conditions for returns and warranty for all brands available.
    This includes specific details for clothing (t-shirts, shorts, blouses) under the AuraLite brand.
    """
    terms = """
---
## AuraLite: Return and Warranty Terms

Thank you for choosing AuraLite products! Your satisfaction is important to us. Please familiarize yourself with our return and warranty terms.

### Return Policy (14-Day Period)

As an online customer, you have the right to **return purchased goods** from AuraLite within **14 calendar days** from the date of receipt of the shipment.

**For a return to be accepted, the following conditions must be met:**

* **Product must be in its original condition:** Clothing must not have been worn, washed, or ironed. It must have all original tags attached and be in its original packaging (if applicable).
* **No signs of use:** The product must not show any signs of use, damage, stains, or alterations that would prevent its resale as new.
* **Shipping costs:** Return shipping costs are at the customer's expense, except in cases of a defective product or an error on AuraLite's part.
* **Refund:** Once we receive and inspect the returned product and confirm it meets all conditions, the amount will be refunded via bank transfer within 14 calendar days from the date of receipt of the returned shipment.

---

### Warranty Terms

AuraLite provides a **30-day warranty** for manufacturing defects on all its clothing (t-shirts, shorts, and blouses), effective from the date of purchase.

**The warranty covers the following cases:**

* Seam unraveling that isn't a result of mechanical damage or improper use/maintenance.
* Fabric defects (e.g., visible holes or fraying not caused by use) that occurred before the garment was washed or worn.
* Zipper or button issues that are a factory defect.

**The warranty does not cover:**

* **Wear and tear:** Products damaged as a result of normal wear and tear, prolonged use, or improper storage.
* **Improper maintenance:** Damage caused by not following the washing and care instructions indicated on the product label.
* **Mechanical damage:** Injuries, tears, stains, or other damage caused by accidents, improper use, misuse, or external factors.
* **Color changes or shrinkage:** If they're a result of improper washing or drying.
* **Products that have been modified or repaired:** By unauthorized persons.

---
---

## StrideNova: Return and Warranty Terms

Thank you for choosing StrideNova products! We value your trust in the quality and durability of our winter apparel. Please familiarize yourself with our return and warranty terms.

### Return Policy (14-Day Period)

As an online customer, you have the right to **return purchased goods** from StrideNova within **14 calendar days** from the date of receipt of the shipment.

**For a return to be accepted, the following conditions must be met:**

* **Product must be in pristine original condition:** Jackets, pants, blouses, and sweaters must not have been worn beyond trying on, washed, or ironed. They must have all original tags attached, original packaging, and accessories (such as spare buttons, drawstrings, hoods, if applicable).
* **No signs of use:** The product must not show any signs of use, damage, stains, odors (e.g., from perfume, cigarettes, or cooking), or alterations that would prevent its resale as new.
* **Shipping costs:** Return shipping costs are at the customer's expense, except in cases of a defective product or an error on StrideNova's part.
* **Refund:** Once we receive and inspect the returned product and confirm it meets all conditions, the amount will be refunded via bank transfer within 14 calendar days from the date of receipt of the returned shipment.

---

### Warranty Terms

StrideNova provides a **60-day warranty** for manufacturing defects on all its winter clothing (jackets, pants, blouses, sweaters), effective from the date of purchase.

**Emphasis on Materials and Quality:**

At StrideNova, we pride ourselves on the carefully selected high-quality materials and robust construction of our products, designed to provide warmth and comfort during colder months. Our warranty terms reflect this commitment to durability.

**The warranty covers the following cases:**

* **Fabric or filling defects:** This includes unintentional fraying of the material, fabric defects leading to a loss of insulation properties (for sweaters and jackets with filling), or uneven distribution of filling that isn't a result of improper maintenance.
* **Seam unraveling:** Including under heavy stress, not caused by mechanical damage or excessive force.
* **Fastener and zipper issues:** Defects in factory zippers, buttons, snap fasteners, or other fastening elements that hinder the garment's functionality.
* **Waterproof properties (for jackets and pants):** In cases where the product is labeled as waterproof/water-repellent, the warranty covers the loss of these properties that isn't a result of mechanical damage to the fabric or improper maintenance (e.g., using unsuitable detergents).

**The warranty does not cover:**

* **Natural wear and tear:** Products damaged as a result of normal wear and tear, prolonged use, or improper storage (e.g., elbow or knee scuffs, color fading over time).
* **Improper maintenance:** Damage caused by not following the washing, drying, and care instructions indicated on the product label. For example, washing a wool sweater at high temperatures, leading to shrinkage.
* **Mechanical damage:** Injuries, tears, holes, burns, stains, or other damage caused by accidents, improper use, misuse, or external factors (e.g., snagging on a sharp object, pet bites).
* **Cosmetic defects:** Minor scratches or changes that do not affect the product's functionality.
* **Products that have been modified or repaired:** By unauthorized persons.
"""
    return terms