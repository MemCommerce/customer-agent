from agents import function_tool


@function_tool
def get_terms_and_conditions(brand: str):
    """
    Retrieves the terms and conditions for returns and warranty for a specific brand.

    Args:
        brand (str): The name of the brand to get information for.
                     Case-sensitive.
    
    Returns:
        str: A string containing the terms and conditions for the specified brand,
             or an error message if the brand is not found.
    """
    
    # Dictionary containing the terms and conditions for each brand.
    # The brand name is the key, and the terms are the value.
    terms_data = {
        "AuraLite": """
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
""",
        "StrideNova": """
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
---
""",
        "Kixora": """
---
## Kixora: Return and Warranty Terms

Welcome to the world of Kixora, where contemporary design meets exceptional comfort. We stand behind the quality of our apparel, underwear, and footwear. Please review our terms to ensure a smooth and satisfactory experience.

### Return Policy (14-Day Period)

As an online customer, you have the right to **return purchased goods** from Kixora within **14 calendar days** from the date of receipt of the shipment.

**For a return to be accepted, the following stringent conditions must be met:**

* **Product must be in its original, unworn condition:** Apparel and footwear must not have been worn (beyond trying on), washed, or altered. They must have all original tags, labels, and be in their original, undamaged packaging (e.g., shoe box).
* **Special Condition for Underwear:** For hygiene reasons, underwear (briefs, boxers, bralettes, etc.) **cannot be returned if the protective seal or original packaging has been opened or tampered with.** Items must be in their sealed, unopened original packaging.
* **Condition of Footwear:** Footwear must be tried on indoors, preferably on a carpeted surface. Shoes with any signs of wear on the soles, scuffs, or creases will not be accepted for return. The original shoe box must be returned without any damage, tape, or labels applied directly to it.
* **No signs of use:** The product must be free of any scents (like perfume or smoke), stains (like makeup or deodorant), or any other signs of use.
* **Shipping costs:** Return shipping costs are at the customer's expense, except in cases of a defective product or an error on Kixora's part.
* **Refund:** Once we receive and inspect the returned product and confirm it meets all conditions, the amount will be refunded via bank transfer within 14 calendar days from the date of receipt of the returned shipment.

---

### Warranty Terms

Kixora provides a **45-day warranty** for manufacturing defects on all its products, including apparel, underwear, and footwear, effective from the date of purchase.

Kixora is synonymous with minimalist aesthetics and superior materials. Our warranty protects against manufacturing flaws that compromise the fit, form, or function of our products.

**The warranty covers the following cases:**

* **For Apparel & Underwear:** Seam integrity issues (unraveling), fabric defects (e.g., runs or holes present before wear), or issues with elastic bands (e.g., premature loss of elasticity not caused by improper washing).
* **For Footwear:** Defects in sole adhesion (sole separation from the upper), faulty stitching, or defective hardware (e.g., eyelets, buckles) that are not the result of force or misuse.
* **For all products:** Faulty zippers, buttons, or clasps that are a result of a factory defect.

**The warranty does not cover:**

* **Normal wear and tear:** This includes fabric pilling from friction, color fading from sun exposure, worn-down soles or heels on footwear from regular use.
* **Improper maintenance:** Damage caused by not following the care instructions on the label (e.g., machine washing a dry-clean-only item, using bleach, improper drying).
* **Mechanical damage:** Tears, snags, stains, scuffs, or any other damage caused by accidents, misuse, or external factors.
* **Fit and comfort after use:** The warranty does not cover issues related to the fit or comfort of a product after it has been worn.
* **Water damage:** On footwear or apparel not explicitly marked as waterproof.
* **Products that have been modified or repaired:** By unauthorized persons.
---
"""
    }
    
    # Check if the requested brand exists in the dictionary
    if brand in terms_data:
        return terms_data[brand]
    else:
        # If the brand is not found, return an error message with the available options
        available_brands = ", ".join(terms_data.keys())
        return (f"Invalid brand specified: '{brand}'.\n"
                f"Please choose from the available options: {available_brands}.")
    

@function_tool
def get_default_terms_and_conditions():
    """
    Provides default return and warranty terms and conditions,
    used when brand-specific data is unavailable.

    Returns:
        str: Default return and warranty information.
    """
    return """
---
## Default: Return and Warranty Terms

These default terms apply to products that do not have brand-specific return or warranty conditions.

### Return Policy (14-Day Period)

As an online customer, you have the right to return goods within **14 calendar days** from the date of receiving the shipment.

**To be eligible for a return, the following conditions must be met:**

- **Product condition:** Items must be unused, unworn, unwashed, and in their original packaging with all tags and labels attached.
- **Packaging:** The original product packaging must be intact and undamaged.
- **Hygiene-sensitive items:** Items such as underwear, swimwear, or personal care products cannot be returned once opened or unsealed.
- **Return shipping:** The customer is responsible for return shipping costs, unless the product is defective or the return is due to an error on our part.
- **Refund timeline:** Refunds will be issued within **14 calendar days** after the returned product has been received and inspected.

---

### Warranty Terms (30 Days)

We offer a **30-day limited warranty** for all products, effective from the date of purchase.

**The warranty covers:**

- Manufacturing defects such as faulty stitching, fabric defects, or broken fasteners.
- Issues affecting the usability of the product due to production flaws.

**The warranty does not cover:**

- Normal wear and tear.
- Damage caused by improper use, accidents, or external factors.
- Damage due to incorrect washing, drying, or storage.
- Altered or repaired products not serviced by authorized personnel.

For any concerns related to returns or warranty claims, please contact our customer service team with your order number and product details.
---
"""