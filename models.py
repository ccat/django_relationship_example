from django.db import models


class TargetClass(models.Model):
    """
    This is a target of OneToOne, ForeignKey and ManyToMany relationships.
    """
    name = models.CharField(max_length=1024,null=True,blank=True)

    def __unicode__(self):
        return unicode(self.name)


class OneToOneClass(models.Model):
    """
    >>> t = TargetClass(name="target")
    >>> t.save()
    >>> o = OneToOneClass(name="OneToOne",target=t)
    >>> o.save()
    >>> t.one_to_one == o
    True
    >>> o.target == t
    True
    >>> o2 = OneToOneClass(name="OneToOne2",target=t)
    >>> o2.save()
    Traceback (most recent call last):
        ...
    IntegrityError: duplicate key value violates unique constraint "django_relationship_example_onetooneclass_target_id_key"
    DETAIL:  Key (target_id)=(4) already exists.
    <BLANKLINE>
    >>> t.one_to_one == o2
    True
    """
    name = models.CharField(max_length=1024,null=True,blank=True)
    target = models.OneToOneField(TargetClass, related_name='one_to_one')


class ForeignKeyClass(models.Model):
    """
    >>> t = TargetClass(name="target")
    >>> t.save()
    >>> f = ForeignKeyClass(name="foreignkey",target=t)
    >>> f.save()
    >>> t.foreignkeys.get(name="foreignkey") == f
    True
    >>> f.target == t
    True
    >>> f2 = ForeignKeyClass(name="foreignkey2",target=t)
    >>> f2.save()
    >>> t.foreignkeys.get(name="foreignkey2") == f2
    True
    """
    name = models.CharField(max_length=1024,null=True,blank=True)
    target = models.ForeignKey(TargetClass, related_name='foreignkeys')


class ManyToManyClass(models.Model):
    """
    >>> t1 = TargetClass(name="target1")
    >>> t1.save()
    >>> t2 = TargetClass(name="target2")
    >>> t2.save()
    >>> m1 = ManyToManyClass(name="ManyToMany1")
    >>> m1.save()
    >>> m2 = ManyToManyClass(name="ManyToMany2")
    >>> m2.save()
    >>> m1.targets.add(t1)
    >>> m1.targets.add(t2)
    >>> m2.targets.add(t1)
    >>> m2.targets.add(t2)
    >>> m1.save()
    >>> m2.save()
    >>> m1.targets.get(name="target1") == t1
    True
    >>> m1.targets.get(name="target2") == t2
    True
    >>> m2.targets.get(name="target1") == t1
    True
    >>> m2.targets.get(name="target2") == t2
    True
    >>> t1.many_to_many.get(name="ManyToMany1") == m1
    True
    >>> t1.many_to_many.get(name="ManyToMany2") == m2
    True
    >>> t2.many_to_many.get(name="ManyToMany1") == m1
    True
    >>> t2.many_to_many.get(name="ManyToMany2") == m2
    True
    """
    name = models.CharField(max_length=1024,null=True,blank=True)
    targets = models.ManyToManyField(TargetClass, related_name='many_to_many')




