import mariadb
import pytest
from models.bands_model import Band

@pytest.fixture
def sample_band():
    # Fixture para obtener el último registro de la base de datos y crear una banda de muestra
    conn = mariadb.connect(
        user="root",
        password="penascal",
        host="127.0.0.1",
        port=3306,
        database="concerts"
    )
    cursor = conn.cursor()

    try:
        query = "SELECT id, bandname, style, website, email FROM bands ORDER BY id DESC LIMIT 1"
        cursor.execute(query)
        row = cursor.fetchone()

        if row:
            band = Band(
                id=row[0],
                bandname=row[1],
                style=row[2],
                website=row[3],
                email=row[4]
            )

            return band
        else:
            return None
    except mariadb.Error as e:
        return None
    finally:
        cursor.close()
        conn.close()


def test_get_bands():
    # Prueba el método get_bands()
    bands, status = Band.get_bands()# Prueba el método patch_band()
    
    assert status == 200
    assert isinstance(bands, list)
    assert len(bands) > 0
    assert all(isinstance(band, dict) for band in bands)

def test_get_band_existing_id(sample_band):
    # Prueba el método get_band() con un ID existente
    band_id = sample_band.id
    band, status = Band.get_band(band_id)
    
    assert status == 200
    assert isinstance(band, dict)
    assert band["id"] == sample_band.id
    assert band["bandname"] == sample_band.bandname
    assert band["style"] == sample_band.style
    assert band["website"] == sample_band.website
    assert band["email"] == sample_band.email

def test_get_band_nonexistent_id():
    # Prueba el método get_band() con un ID inexistente
    band_id = 1000
    band, status = Band.get_band(band_id)
    assert status == 404
    assert isinstance(band, dict)
    assert band["message"] == "404 Band not found"

def test_post_band():
    # Prueba el método post_band()
    band_data = {
        "bandname": "Abbaq2",
        "style": "Pop",
        "website": "www.dancingqueen.com",
        "email": "dancing@queen.com"
    }
    response, status = Band.post_band(band_data)
    assert status == 200
    assert isinstance(response, dict)
    assert response["message"] == "Band created successfully"

def test_put_band(sample_band):
    # Prueba el método put_band()
    band_id = sample_band.id
    new_band_data = {
        "bandname": "UpdatedBand",
        "style": "Metal",
        "website": "www.updatedband.com",
        "email": "info@updatedband.com"
    }
    response, status = Band.put_band(new_band_data, band_id)
    assert status == 200
    assert isinstance(response, dict)
    assert response["message"] == "Band updated successfully"

def test_patch_band(sample_band):
    # Prueba el método patch_band()
    band_id = sample_band.id
    updated_fields = {
        "bandname": sample_band.bandname,
        "style": sample_band.style
    }
    response, status = Band.patch_band(updated_fields, band_id)
    assert status == 200
    assert isinstance(response, dict)
    assert response["message"] == "Band updated successfully"

def test_delete_band(sample_band):
     # Prueba el método delete_band()
     band_id = sample_band.id
     response, status = Band.delete_band(band_id)
     assert status == 200
     assert isinstance(response, dict)
     assert response["message"] == "Band deleted successfully"
