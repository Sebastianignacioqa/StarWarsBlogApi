"""empty message

Revision ID: 03c7857df4c3
Revises: 824c7c370d22
Create Date: 2021-09-17 23:58:55.838555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03c7857df4c3'
down_revision = '824c7c370d22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('hair_color', sa.String(length=200), nullable=True),
    sa.Column('skin_color', sa.String(length=200), nullable=True),
    sa.Column('eye_color', sa.String(length=200), nullable=True),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(length=200), nullable=True),
    sa.Column('homeworld', sa.Integer(), nullable=True),
    sa.Column('vehicles_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['homeworld'], ['planets.planet_id'], ),
    sa.ForeignKeyConstraint(['vehicles_id'], ['vehicles.vehicle_id'], ),
    sa.PrimaryKeyConstraint('character_id')
    )
    op.create_table('planets',
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('climate', sa.String(length=200), nullable=True),
    sa.Column('terrain', sa.String(length=200), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('diameter', sa.Integer(), nullable=True),
    sa.Column('rotation_period', sa.Integer(), nullable=True),
    sa.Column('orbital_period', sa.Integer(), nullable=True),
    sa.Column('surface_water', sa.Integer(), nullable=True),
    sa.Column('residents', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['residents'], ['characters.character_id'], ),
    sa.PrimaryKeyConstraint('planet_id')
    )
    op.create_table('vehicles',
    sa.Column('vehicle_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('model', sa.String(length=200), nullable=True),
    sa.Column('manufacturer', sa.String(length=200), nullable=True),
    sa.Column('cost_in_credits', sa.Integer(), nullable=True),
    sa.Column('crew', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('cargo_capacity', sa.Integer(), nullable=True),
    sa.Column('vehicle_class', sa.String(length=200), nullable=True),
    sa.Column('pilots', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pilots'], ['characters.character_id'], ),
    sa.PrimaryKeyConstraint('vehicle_id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('fav_planet_id', sa.Integer(), nullable=True),
    sa.Column('fav_character_id', sa.Integer(), nullable=True),
    sa.Column('fav_vehicle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fav_character_id'], ['characters.character_id'], ),
    sa.ForeignKeyConstraint(['fav_planet_id'], ['planets.planet_id'], ),
    sa.ForeignKeyConstraint(['fav_vehicle_id'], ['vehicles.vehicle_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    op.drop_table('vehicles')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###
