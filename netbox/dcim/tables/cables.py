import django_tables2 as tables
from django_tables2.utils import Accessor

from dcim.models import Cable
from tenancy.tables import TenantColumn
from utilities.tables import BaseTable, ChoiceFieldColumn, ColorColumn, TagColumn, TemplateColumn, ToggleColumn
from .template_code import CABLE_LENGTH, CABLE_TERMINATION_PARENT

__all__ = (
    'CableTable',
)


#
# Cables
#

class CableTable(BaseTable):
    pk = ToggleColumn()
    termination_a_parent = tables.TemplateColumn(
        template_code=CABLE_TERMINATION_PARENT,
        accessor=Accessor('termination_a'),
        orderable=False,
        verbose_name='Side A'
    )
    rack_a = tables.Column(
        accessor=Accessor('termination_a__device__rack'),
        orderable=False,
        linkify=True,
        verbose_name='Rack A'
    )
    termination_a = tables.Column(
        accessor=Accessor('termination_a'),
        orderable=False,
        linkify=True,
        verbose_name='Termination A'
    )
    termination_b_parent = tables.TemplateColumn(
        template_code=CABLE_TERMINATION_PARENT,
        accessor=Accessor('termination_b'),
        orderable=False,
        verbose_name='Side B'
    )
    rack_b = tables.Column(
        accessor=Accessor('termination_b__device__rack'),
        orderable=False,
        linkify=True,
        verbose_name='Rack B'
    )
    termination_b = tables.Column(
        accessor=Accessor('termination_b'),
        orderable=False,
        linkify=True,
        verbose_name='Termination B'
    )
    status = ChoiceFieldColumn()
    tenant = TenantColumn()
    length = TemplateColumn(
        template_code=CABLE_LENGTH,
        order_by=('_abs_length', 'length_unit')
    )
    color = ColorColumn()
    tags = TagColumn(
        url_name='dcim:cable_list'
    )

    class Meta(BaseTable.Meta):
        model = Cable
        fields = (
            'pk', 'id', 'label', 'termination_a_parent', 'rack_a', 'termination_a', 'termination_b_parent', 'rack_b', 'termination_b',
            'status', 'type', 'tenant', 'color', 'length', 'tags', 'created', 'last_updated',
        )
        default_columns = (
            'pk', 'id', 'label', 'termination_a_parent', 'termination_a', 'termination_b_parent', 'termination_b',
            'status', 'type',
        )
